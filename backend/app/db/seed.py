from sqlmodel import Session, select
from app.db.database import engine
from app.db.models_base import Rol, EstadoPedido, FormaPago

def seed_data():
    with Session(engine) as session:
        # Seed Roles
        roles = [
            Rol(codigo="ADMIN", descripcion="Administrador del sistema"),
            Rol(codigo="STOCK", descripcion="Gestor de stock"),
            Rol(codigo="PEDIDOS", descripcion="Gestor de pedidos"),
            Rol(codigo="CLIENT", descripcion="Cliente final"),
        ]
        for rol in roles:
            existing = session.get(Rol, rol.codigo)
            if not existing:
                session.add(rol)

        # Seed Estados de Pedido
        estados = [
            EstadoPedido(codigo="PENDIENTE", descripcion="Pedido creado, pago pendiente", orden=1, es_terminal=False),
            EstadoPedido(codigo="CONFIRMADO", descripcion="Pago confirmado", orden=2, es_terminal=False),
            EstadoPedido(codigo="EN_PREP", descripcion="En preparación en cocina", orden=3, es_terminal=False),
            EstadoPedido(codigo="EN_CAMINO", descripcion="Despachado al cliente", orden=4, es_terminal=False),
            EstadoPedido(codigo="ENTREGADO", descripcion="Entrega confirmada", orden=5, es_terminal=True),
            EstadoPedido(codigo="CANCELADO", descripcion="Pedido cancelado", orden=6, es_terminal=True),
        ]
        for estado in estados:
            existing = session.get(EstadoPedido, estado.codigo)
            if not existing:
                session.add(estado)

        # Seed Formas de Pago
        formas = [
            FormaPago(codigo="MERCADOPAGO", descripcion="Pago via MercadoPago", habilitado=True),
            FormaPago(codigo="EFECTIVO", descripcion="Pago en efectivo", habilitado=True),
            FormaPago(codigo="TRANSFERENCIA", descripcion="Transferencia bancaria", habilitado=True),
        ]
        for forma in formas:
            existing = session.get(FormaPago, forma.codigo)
            if not existing:
                session.add(forma)

        session.commit()
        print("Seed data loaded successfully!")

if __name__ == "__main__":
    seed_data()
