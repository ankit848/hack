import click

@click.command()
@click.option('--name', prompt='Enter the name of the bonnet', help='Name of the network bonnet')
@click.option('--type', prompt='Enter the type of the bonnet', help='Type of the network bonnet')
@click.option('--ip', prompt='Enter the IP address of the bonnet', help='IP address of the network bonnet')
def create_bonnet(name, type, ip):
    """
    Create a new network bonnet with the specified name, type, and IP address.
    """
    # Here you can write code to create the network bonnet
    # This could involve generating configuration files, setting up networking settings, etc.
    
    click.echo(f'Creating network bonnet "{name}" of type "{type}" with IP address "{ip}"...')
    # Example: Write configuration to a file
    with open(f'{name}_config.txt', 'w') as f:
        f.write(f'Name: {name}\nType: {type}\nIP Address: {ip}')
    
    click.echo('Network bonnet created successfully!')

if __name__ == '__main__':
    create_bonnet()
