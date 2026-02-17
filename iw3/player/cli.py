from .server import server_main as backend_main, create_parser, set_state_args


def main():
    parser = create_parser()
    args = parser.parse_args()
    set_state_args(args)
    backend_main(args)


if __name__ == "__main__":
    main()
