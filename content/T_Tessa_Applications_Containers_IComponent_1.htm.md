# IComponent<TOperation> \- интерфейс
Описание интерфейса компонента
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers](N_Tessa_Applications_Containers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IComponent<in TOperation> : IComponent
    where TOperation : class, IOperationVisitor
VB __Копировать
     Public Interface IComponent(Of In TOperation As {Class, IOperationVisitor})
    	Inherits IComponent
C++ __Копировать
    generic<typename TOperation>
    where TOperation : ref class, IOperationVisitor
    public interface class IComponent : IComponent
F# __Копировать
     type IComponent<'TOperation when 'TOperation : not struct and IOperationVisitor> = 
        interface
            interface IComponent
        end
Implements
    [IComponent](T_Tessa_Applications_Containers_IComponent.htm)
#### Параметры типа
TOperation
     Тип операции 
## __Свойства
[Parent](P_Tessa_Applications_Containers_IComponent_Parent.htm)|  Gets or sets
Родитель/Владелец  
(Унаследован от [IComponent](T_Tessa_Applications_Containers_IComponent.htm))  
---|---  
##  __Методы
[Accept](M_Tessa_Applications_Containers_IComponent_1_Accept.htm)|  Вызывает
выполнение операции operation над текущим узлом  
---|---  
[GetFullyQualifiedName](M_Tessa_Applications_Containers_IComponent_GetFullyQualifiedName.htm)|
Возвращает полное имя объекта  
(Унаследован от [IComponent](T_Tessa_Applications_Containers_IComponent.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications.Containers - пространство
имён](N_Tessa_Applications_Containers.htm)
