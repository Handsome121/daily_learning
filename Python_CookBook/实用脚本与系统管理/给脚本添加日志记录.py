import logging
import logging.config


def main():
    # logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(levelname)s:%(asctime)s:%(message)')
    logging.config.fileConfig('logconfig.ini')
    hostname = 'www.python.org'
    item = 'span'
    mode = 'r'
    filename = 'test.py'
    logging.critical('Host %s unknown', hostname)
    logging.error('could not find %r', item)
    logging.warning('feature is deprecated')
    logging.info('opening file %s,mode=%r', filename, mode)
    logging.debug('got here')


if __name__ == '__main__':
    main()
