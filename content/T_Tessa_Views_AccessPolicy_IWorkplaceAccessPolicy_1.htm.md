# IWorkplaceAccessPolicy<TContext> \- интерфейс
Описание интерфейса политики доступности для обработки метаданных раочих мест
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkplaceAccessPolicy<TContext> : IAccessPolicy<IWorkplaceComponentMetadata, TContext>
VB __Копировать
     Public Interface IWorkplaceAccessPolicy(Of TContext)
    	Inherits IAccessPolicy(Of IWorkplaceComponentMetadata, TContext)
C++ __Копировать
    generic<typename TContext>
    public interface class IWorkplaceAccessPolicy : IAccessPolicy<IWorkplaceComponentMetadata^, TContext>
F# __Копировать
     type IWorkplaceAccessPolicy<'TContext> = 
        interface
            interface IAccessPolicy<IWorkplaceComponentMetadata, 'TContext>
        end
Implements
    [IAccessPolicy](T_Tessa_Views_AccessPolicy_IAccessPolicy_2.htm)<[IWorkplaceComponentMetadata](T_Tessa_Views_Workplaces_IWorkplaceComponentMetadata.htm), TContext>
#### Параметры типа
TContext
     Тип контекста 
## __Методы
[AddRules](M_Tessa_Views_AccessPolicy_IAccessPolicy_2_AddRules.htm)|
Добавляет правила в политику безопасности  
(Унаследован от [IAccessPolicy<TAccessSubject,
TContext>](T_Tessa_Views_AccessPolicy_IAccessPolicy_2.htm))  
---|---  
[IsSatisfiedByAsync](M_Tessa_Views_AccessPolicy_IAccessPolicy_2_IsSatisfiedByAsync.htm)|
Осуществляет проверку доступности элемента subject в соответствии с правилами
политик доступа.  
(Унаследован от [IAccessPolicy<TAccessSubject,
TContext>](T_Tessa_Views_AccessPolicy_IAccessPolicy_2.htm))  
##  __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
