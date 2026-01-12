from __future__ import annotations

import sys


def main() -> int:
    if '-h' in sys.argv or '--help' in sys.argv:
        from twitch.constants.help import HELP_TEXT

        print(HELP_TEXT)  # noqa: T201
        return 0

    import asyncio
    import logging

    import twitch._exceptions as exc
    from twitch import logger
    from twitch import setup

    args = setup.args()

    logger.verbose(args.verbose)
    log = logging.getLogger(__name__)
    if args.verbose:
        log.debug('arguments: %s', vars(args))

    menu = setup.menu(args)

    try:
        run = asyncio.run
        twitch = run(setup.app(menu, args))
        twitch = setup.keybinds(twitch)

        if args.test:
            return run(setup.test(t=twitch))
        if args.channel:
            return run(twitch.show_by_query())
        if args.games:
            return run(twitch.show_by_game())
        return run(twitch.show_all_streams())

    except (*exc.CONNECTION_EXCEPTION, *exc.EXCEPTIONS) as err:
        menu.keybind.unregister_all()
        menu.select(items=[f'{err!r}'], markup=False, prompt='PyTwitchErr>')
        log.error(err)

    except KeyboardInterrupt:
        log.info('terminated by user')

    return 1


if __name__ == '__main__':
    sys.exit(main())
