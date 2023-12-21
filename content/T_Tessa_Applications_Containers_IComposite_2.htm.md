# IComposite<TComponent, TOperation> \- интерфейс
Описание интерфейса композитного контейнера Над объектами контейнера могут
быть совершены операции TOperation. Данный контейнер поддерживает хранение
компонентов типа TComponent.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers](N_Tessa_Applications_Containers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IComposite<TComponent, in TOperation> : IComponent<TOperation>, 
    	IComponent
    where TComponent : class, Object, IComponent<TOperation>
    where TOperation : class, IOperationVisitor
VB __Копировать
     Public Interface IComposite(Of TComponent As {Class, Object, IComponent(Of TOperation)}, In TOperation As {Class, IOperationVisitor})
    	Inherits IComponent(Of TOperation), IComponent
C++ __Копировать
    generic<typename TComponent, typename TOperation>
    where TComponent : ref class, Object, IComponent<TOperation>
    where TOperation : ref class, IOperationVisitor
    public interface class IComposite : IComponent<TOperation>, 
    	IComponent
F# __Копировать
     type IComposite<'TComponent, 'TOperation when 'TComponent : not struct and Object and IComponent<'TOperation> when 'TOperation : not struct and IOperationVisitor> = 
        interface
            interface IComponent<'TOperation>
            interface IComponent
        end
Implements
    [IComponent](T_Tessa_Applications_Containers_IComponent.htm), [IComponent](T_Tessa_Applications_Containers_IComponent_1.htm)<TOperation>
#### Параметры типа
TComponent
     Тип компонента контейнера 
TOperation
     Тип операции над контейнером и его элементами 
## __Свойства
[Components](P_Tessa_Applications_Containers_IComposite_2_Components.htm)|
Gets Возвращает список компонентов контейнера расположенных непосредственно в
самом контейнере.  
---|---  
[Parent](P_Tessa_Applications_Containers_IComponent_Parent.htm)|  Gets or sets
Родитель/Владелец  
(Унаследован от [IComponent](T_Tessa_Applications_Containers_IComponent.htm))  
##  __Методы
[Accept](M_Tessa_Applications_Containers_IComponent_1_Accept.htm)|  Вызывает
выполнение операции operation над текущим узлом  
(Унаследован от
[IComponent<TOperation>](T_Tessa_Applications_Containers_IComponent_1.htm))  
---|---  
[AddComponent](M_Tessa_Applications_Containers_IComposite_2_AddComponent.htm)|
Добавляет компонент component в контейнер. Добавляемый компонент должен быть
не равен null.  
[ClearComponents](M_Tessa_Applications_Containers_IComposite_2_ClearComponents.htm)|
Осуществляет удаление из контейнера всех элементов  
[GetFullyQualifiedName](M_Tessa_Applications_Containers_IComponent_GetFullyQualifiedName.htm)|
Возвращает полное имя объекта  
(Унаследован от [IComponent](T_Tessa_Applications_Containers_IComponent.htm))  
[RemoveComponent](M_Tessa_Applications_Containers_IComposite_2_RemoveComponent.htm)|
Удаляет компонент component из контейнера. Удаляемый компонент должен быть не
равен null  
## __См. также
#### Ссылки
[Tessa.Applications.Containers - пространство
имён](N_Tessa_Applications_Containers.htm)
