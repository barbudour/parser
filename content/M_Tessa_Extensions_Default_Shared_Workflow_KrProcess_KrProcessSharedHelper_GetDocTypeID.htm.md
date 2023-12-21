# KrProcessSharedHelper.GetDocTypeID - метод
Возвращает идентификатор типа документа для заданной карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Guid? GetDocTypeID(
    	Card card
    )
VB __Копировать
     Public Shared Function GetDocTypeID ( 
    	card As Card
    ) As Guid?
C++ __Копировать
     public:
    static Nullable<Guid> GetDocTypeID(
    	Card^ card
    )
F# __Копировать
     static member GetDocTypeID : 
            card : Card -> Nullable<Guid> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется получить идентификатор типа документа.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Идентификатор типа документа или значение null, если его не удалось получить.
##  __Заметки
Метод не выполняет запросов к базе данных.
##  __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
