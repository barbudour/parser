# IWorkplaceAccessRule<TContext> \- интерфейс
Описание интерфейса правила доступности для метаданных рабочего места
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkplaceAccessRule<in TContext> : IAccessRule<IWorkplaceComponentMetadata, TContext>
VB __Копировать
     Public Interface IWorkplaceAccessRule(Of In TContext)
    	Inherits IAccessRule(Of IWorkplaceComponentMetadata, TContext)
C++ __Копировать
    generic<typename TContext>
    public interface class IWorkplaceAccessRule : IAccessRule<IWorkplaceComponentMetadata^, TContext>
F# __Копировать
     type IWorkplaceAccessRule<'TContext> = 
        interface
            interface IAccessRule<IWorkplaceComponentMetadata, 'TContext>
        end
Implements
    [IAccessRule](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm)<[IWorkplaceComponentMetadata](T_Tessa_Views_Workplaces_IWorkplaceComponentMetadata.htm), TContext>
#### Параметры типа
TContext
     Тип контекста 
## __Методы
[IsSatisfiedByAsync](M_Tessa_Views_AccessPolicy_IAccessRule_2_IsSatisfiedByAsync.htm)|
Выполняет проверку доступности объекта subject  
(Унаследован от [IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
