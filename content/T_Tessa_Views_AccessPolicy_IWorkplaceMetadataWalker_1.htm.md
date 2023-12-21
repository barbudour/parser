# IWorkplaceMetadataWalker<TMandatoryContext> \- интерфейс
Описание интерфейса для объектов осуществляющих обработку метаданных рабочих
мест
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkplaceMetadataWalker<TMandatoryContext>
VB __Копировать
     Public Interface IWorkplaceMetadataWalker(Of TMandatoryContext)
C++ __Копировать
    generic<typename TMandatoryContext>
    public interface class IWorkplaceMetadataWalker
F# __Копировать
     type IWorkplaceMetadataWalker<'TMandatoryContext> = interface end
#### Параметры типа
TMandatoryContext
     Тип контекста 
## __Методы
[ApplyAsync(IWorkplaceMetadata, TMandatoryContext,
CancellationToken)](M_Tessa_Views_AccessPolicy_IWorkplaceMetadataWalker_1_ApplyAsync.htm)|
Обрабатывает метаданные рабочего места metadata в соответствии с правилами
политики
[IWorkplaceAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IWorkplaceAccessPolicy_1.htm)
и контекстом context  
---|---  
[ApplyAsync(IWorkplaceMetadata, TMandatoryContext,
AccessRuleExecutor<IWorkplaceComponentMetadata, TMandatoryContext>,
CancellationToken)](M_Tessa_Views_AccessPolicy_IWorkplaceMetadataWalker_1_ApplyAsync_1.htm)|
Обрабатывает метаданные рабочего места metadata в соответствии с правилами
политики
[IWorkplaceAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IWorkplaceAccessPolicy_1.htm)
и контекстом context  
##  __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
