from netbox.registry import registry
from . import *


#
# Nav menus
#

ORGANIZATION_MENU = Menu(
    label='Organization',
    icon_class='mdi mdi-domain',
    groups=(
        MenuGroup(
            label='Sites',
            items=(
                get_model_item('dcim', 'site', 'Sites'),
                get_model_item('dcim', 'region', 'Regions'),
                get_model_item('dcim', 'sitegroup', 'Site Groups'),
                get_model_item('dcim', 'location', 'Locations'),
            ),
        ),
        MenuGroup(
            label='Racks',
            items=(
                get_model_item('dcim', 'rack', 'Racks'),
                get_model_item('dcim', 'rackrole', 'Rack Roles'),
                get_model_item('dcim', 'rackreservation', 'Reservations'),
                MenuItem(
                    link='dcim:rack_elevation_list',
                    link_text='Elevations',
                    permissions=['dcim.view_rack']
                ),
            ),
        ),
        MenuGroup(
            label='Tenancy',
            items=(
                get_model_item('tenancy', 'tenant', 'Tenants'),
                get_model_item('tenancy', 'tenantgroup', 'Tenant Groups'),
            ),
        ),
        MenuGroup(
            label='Contacts',
            items=(
                get_model_item('tenancy', 'contact', 'Contacts'),
                get_model_item('tenancy', 'contactgroup', 'Contact Groups'),
                get_model_item('tenancy', 'contactrole', 'Contact Roles'),
            ),
        ),
    ),
)

DEVICES_MENU = Menu(
    label='Devices',
    icon_class='mdi mdi-server',
    groups=(
        MenuGroup(
            label='Devices',
            items=(
                get_model_item('dcim', 'device', 'Devices'),
                get_model_item('dcim', 'virtualdevicecontext', 'Virtual Device Contexts'),
                get_model_item('dcim', 'module', 'Modules'),
                get_model_item('dcim', 'devicerole', 'Device Roles'),
                get_model_item('dcim', 'platform', 'Platforms'),
                get_model_item('dcim', 'virtualchassis', 'Virtual Chassis'),
            ),
        ),
        MenuGroup(
            label='Device Types',
            items=(
                get_model_item('dcim', 'devicetype', 'Device Types'),
                get_model_item('dcim', 'moduletype', 'Module Types'),
                get_model_item('dcim', 'manufacturer', 'Manufacturers'),
            ),
        ),
        MenuGroup(
            label='Device Components',
            items=(
                get_model_item('dcim', 'interface', 'Interfaces', actions=['import']),
                get_model_item('dcim', 'frontport', 'Front Ports', actions=['import']),
                get_model_item('dcim', 'rearport', 'Rear Ports', actions=['import']),
                get_model_item('dcim', 'consoleport', 'Console Ports', actions=['import']),
                get_model_item('dcim', 'consoleserverport', 'Console Server Ports', actions=['import']),
                get_model_item('dcim', 'powerport', 'Power Ports', actions=['import']),
                get_model_item('dcim', 'poweroutlet', 'Power Outlets', actions=['import']),
                get_model_item('dcim', 'modulebay', 'Module Bays', actions=['import']),
                get_model_item('dcim', 'devicebay', 'Device Bays', actions=['import']),
                get_model_item('dcim', 'inventoryitem', 'Inventory Items', actions=['import']),
                get_model_item('dcim', 'inventoryitemrole', 'Inventory Item Roles'),
            ),
        ),
    ),
)

CONNECTIONS_MENU = Menu(
    label='Connections',
    icon_class='mdi mdi-connection',
    groups=(
        MenuGroup(
            label='Connections',
            items=(
                get_model_item('dcim', 'cable', 'Cables', actions=['import']),
                get_model_item('wireless', 'wirelesslink', 'Wireless Links', actions=['import']),
                MenuItem(
                    link='dcim:interface_connections_list',
                    link_text='Interface Connections',
                    permissions=['dcim.view_interface']
                ),
                MenuItem(
                    link='dcim:console_connections_list',
                    link_text='Console Connections',
                    permissions=['dcim.view_consoleport']
                ),
                MenuItem(
                    link='dcim:power_connections_list',
                    link_text='Power Connections',
                    permissions=['dcim.view_powerport']
                ),
            ),
        ),
    ),
)

WIRELESS_MENU = Menu(
    label='Wireless',
    icon_class='mdi mdi-wifi',
    groups=(
        MenuGroup(
            label='Wireless',
            items=(
                get_model_item('wireless', 'wirelesslan', 'Wireless LANs'),
                get_model_item('wireless', 'wirelesslangroup', 'Wireless LAN Groups'),
            ),
        ),
    ),
)

IPAM_MENU = Menu(
    label='IPAM',
    icon_class='mdi mdi-counter',
    groups=(
        MenuGroup(
            label='IP Addresses',
            items=(
                get_model_item('ipam', 'ipaddress', 'IP Addresses'),
                get_model_item('ipam', 'iprange', 'IP Ranges'),
            ),
        ),
        MenuGroup(
            label='Prefixes',
            items=(
                get_model_item('ipam', 'prefix', 'Prefixes'),
                get_model_item('ipam', 'role', 'Prefix & VLAN Roles'),
            ),
        ),
        MenuGroup(
            label='ASNs',
            items=(
                get_model_item('ipam', 'asn', 'ASNs'),
            ),
        ),
        MenuGroup(
            label='Aggregates',
            items=(
                get_model_item('ipam', 'aggregate', 'Aggregates'),
                get_model_item('ipam', 'rir', 'RIRs'),
            ),
        ),
        MenuGroup(
            label='VRFs',
            items=(
                get_model_item('ipam', 'vrf', 'VRFs'),
                get_model_item('ipam', 'routetarget', 'Route Targets'),
            ),
        ),
        MenuGroup(
            label='VLANs',
            items=(
                get_model_item('ipam', 'vlan', 'VLANs'),
                get_model_item('ipam', 'vlangroup', 'VLAN Groups'),
            ),
        ),
        MenuGroup(
            label='Other',
            items=(
                get_model_item('ipam', 'fhrpgroup', 'FHRP Groups'),
                get_model_item('ipam', 'servicetemplate', 'Service Templates'),
                get_model_item('ipam', 'service', 'Services'),
            ),
        ),
    ),
)

OVERLAY_MENU = Menu(
    label='Overlay',
    icon_class='mdi mdi-graph-outline',
    groups=(
        MenuGroup(
            label='L2VPNs',
            items=(
                get_model_item('ipam', 'l2vpn', 'L2VPNs'),
                get_model_item('ipam', 'l2vpntermination', 'Terminations'),
            ),
        ),
    ),
)

VIRTUALIZATION_MENU = Menu(
    label='Virtualization',
    icon_class='mdi mdi-monitor',
    groups=(
        MenuGroup(
            label='Virtual Machines',
            items=(
                get_model_item('virtualization', 'virtualmachine', 'Virtual Machines'),
                get_model_item('virtualization', 'vminterface', 'Interfaces', actions=['import']),
            ),
        ),
        MenuGroup(
            label='Clusters',
            items=(
                get_model_item('virtualization', 'cluster', 'Clusters'),
                get_model_item('virtualization', 'clustertype', 'Cluster Types'),
                get_model_item('virtualization', 'clustergroup', 'Cluster Groups'),
            ),
        ),
    ),
)

CIRCUITS_MENU = Menu(
    label='Circuits',
    icon_class='mdi mdi-transit-connection-variant',
    groups=(
        MenuGroup(
            label='Circuits',
            items=(
                get_model_item('circuits', 'circuit', 'Circuits'),
                get_model_item('circuits', 'circuittype', 'Circuit Types'),
            ),
        ),
        MenuGroup(
            label='Providers',
            items=(
                get_model_item('circuits', 'provider', 'Providers'),
                get_model_item('circuits', 'providernetwork', 'Provider Networks'),
            ),
        ),
    ),
)

POWER_MENU = Menu(
    label='Power',
    icon_class='mdi mdi-flash',
    groups=(
        MenuGroup(
            label='Power',
            items=(
                get_model_item('dcim', 'powerfeed', 'Power Feeds'),
                get_model_item('dcim', 'powerpanel', 'Power Panels'),
            ),
        ),
    ),
)

OTHER_MENU = Menu(
    label='Other',
    icon_class='mdi mdi-notification-clear-all',
    groups=(
        MenuGroup(
            label='Logging',
            items=(
                get_model_item('extras', 'journalentry', 'Journal Entries', actions=[]),
                get_model_item('extras', 'objectchange', 'Change Log', actions=[]),
            ),
        ),
        MenuGroup(
            label='Customization',
            items=(
                get_model_item('extras', 'customfield', 'Custom Fields'),
                get_model_item('extras', 'customlink', 'Custom Links'),
                get_model_item('extras', 'exporttemplate', 'Export Templates'),
                get_model_item('extras', 'savedfilter', 'Saved Filters'),
            ),
        ),
        MenuGroup(
            label='Integrations',
            items=(
                get_model_item('extras', 'webhook', 'Webhooks'),
                MenuItem(
                    link='extras:report_list',
                    link_text='Reports',
                    permissions=['extras.view_report']
                ),
                MenuItem(
                    link='extras:script_list',
                    link_text='Scripts',
                    permissions=['extras.view_script']
                ),
                MenuItem(
                    link='extras:jobresult_list',
                    link_text='Job Results',
                    permissions=['extras.view_jobresult'],
                ),
            ),
        ),
        MenuGroup(
            label='Other',
            items=(
                get_model_item('extras', 'tag', 'Tags'),
                get_model_item('extras', 'configcontext', 'Config Contexts', actions=['add']),
            ),
        ),
    ),
)


MENUS = [
    ORGANIZATION_MENU,
    DEVICES_MENU,
    CONNECTIONS_MENU,
    WIRELESS_MENU,
    IPAM_MENU,
    OVERLAY_MENU,
    VIRTUALIZATION_MENU,
    CIRCUITS_MENU,
    POWER_MENU,
    OTHER_MENU,
]

#
# Add plugin menus
#

for menu in registry['plugins']['menus']:
    MENUS.append(menu)

if registry['plugins']['menu_items']:

    # Build the default plugins menu
    groups = [
        MenuGroup(label=label, items=items)
        for label, items in registry['plugins']['menu_items'].items()
    ]
    plugins_menu = Menu(
        label="Plugins",
        icon_class="mdi mdi-puzzle",
        groups=groups
    )
    MENUS.append(plugins_menu)
