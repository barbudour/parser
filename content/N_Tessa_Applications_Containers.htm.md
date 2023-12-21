# Tessa.Applications.Containers - пространство имён
API управления приложениями в части контейнеров приложений - объектов с XML-
описанием файлов, входящих в приложение.
##  __Классы
[OperationContext](T_Tessa_Applications_Containers_OperationContext.htm)|
Класс реализующий контекст
[IOperationContext](T_Tessa_Applications_Containers_IOperationContext.htm) для
операций
[IOperationVisitor](T_Tessa_Applications_Containers_IOperationVisitor.htm)  
---|---  
##  __Интерфейсы
[IApplicationCollection](T_Tessa_Applications_Containers_IApplicationCollection.htm)|
Описание интерфейса коллекции приложений  
---|---  
[IComponent](T_Tessa_Applications_Containers_IComponent.htm)|  Описание
интерфейса компонента системы
[IComponent](T_Tessa_Applications_Containers_IComponent.htm)  
[IComponent<TOperation>](T_Tessa_Applications_Containers_IComponent_1.htm)|
Описание интерфейса компонента  
[IComponentCloneable](T_Tessa_Applications_Containers_IComponentCloneable.htm)|
The ComponentCloneable interface.  
[IComposite<TComponent,
TOperation>](T_Tessa_Applications_Containers_IComposite_2.htm)|  Описание
интерфейса композитного контейнера Над объектами контейнера могут быть
совершены операции TOperation. Данный контейнер поддерживает хранение
компонентов типа TComponent.  
[IOperationContext](T_Tessa_Applications_Containers_IOperationContext.htm)|
Описание интерфейс контекста операции над
[IComponent<TOperation>](T_Tessa_Applications_Containers_IComponent_1.htm) с
помощью
[IOperationVisitor](T_Tessa_Applications_Containers_IOperationVisitor.htm)  
[IOperationVisitor](T_Tessa_Applications_Containers_IOperationVisitor.htm)|
Описание интерфейса выполнения операции над компонентами типа
[IComponent<TOperation>](T_Tessa_Applications_Containers_IComponent_1.htm)
