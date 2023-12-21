# IStorageElementOperationVisitor - интерфейс
Интерфейс описания операции над хранилищем
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IStorageElementOperationVisitor : IOperationVisitor
VB __Копировать
     Public Interface IStorageElementOperationVisitor
    	Inherits IOperationVisitor
C++ __Копировать
     public interface class IStorageElementOperationVisitor : IOperationVisitor
F# __Копировать
     type IStorageElementOperationVisitor = 
        interface
            interface IOperationVisitor
        end
Implements
    [IOperationVisitor](T_Tessa_Applications_Containers_IOperationVisitor.htm)
##  __Методы
[VisitEnterContainer](M_Tessa_Applications_Containers_Storage_IStorageElementOperationVisitor_VisitEnterContainer.htm)|
Вызывается при обработке входа в контейнер хранилища  
---|---  
[VisitLeaveContainer](M_Tessa_Applications_Containers_Storage_IStorageElementOperationVisitor_VisitLeaveContainer.htm)|
Вызывается при обработке выхода из контейнера хранилища  
## __См. также
#### Ссылки
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
