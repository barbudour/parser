# DefaultExtensionHelper.GetDocTypeInfoAsync - метод
Возвращает информацию по типу карточки и типу документа (если он присутствует)
для карточки с заданными идентификатором. Возвращает результат выполнения
запроса. Поскольку запрос расширяемый, то даже при успешном запросе (т.е. при
отсутствии расширений) возвращаемые out-параметры могут быть равны null.
Возвращает cardTypeID \- идентификатор типа карточки, полученный по
идентификатору карточки cardID, или null, если карточка с таким
идентификатором не существует
Возвращает docTypeID \- идентификатор типа документа, полученный по
идентификатору карточки cardID, или null, если либо карточка с таким
идентификатором не существует, либо тип карточки не добавлен в типовое
решение, либо тип карточки не поддерживает типы документов.
Возвращает docTypeTitle \- отображаемое название типа документа, полученное по
идентификатору карточки cardID, или null, если либо карточка с таким
идентификатором не существует, либо тип карточки не добавлен в типовое
решение, либо тип карточки не поддерживает типы документов
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared](N_Tessa_Extensions_Default_Shared.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<(ValidationResult result, Guid? cardTypeID, Guid? docTypeID, string docTypeTitle)> GetDocTypeInfoAsync(
    	ICardRepository extendedRepository,
    	Guid cardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetDocTypeInfoAsync ( 
    	extendedRepository As ICardRepository,
    	cardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (result As ValidationResult, cardTypeID As Guid?, docTypeID As Guid?, docTypeTitle As String))
C++ __Копировать
     public:
    static Task<ValueTuple<ValidationResult^, Nullable<Guid>, Nullable<Guid>, String^>>^ GetDocTypeInfoAsync(
    	ICardRepository^ extendedRepository, 
    	Guid cardID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetDocTypeInfoAsync : 
            extendedRepository : ICardRepository * 
            cardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<ValidationResult, Nullable<Guid>, Nullable<Guid>, string>> 
#### Параметры
extendedRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточки с расширениями.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой возвращается информация.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-4)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm),
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>,
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>,
[String](https://learn.microsoft.com/dotnet/api/system.string)>>  
Результат выполнения запроса.
##  __См. также
#### Ссылки
[DefaultExtensionHelper -
](T_Tessa_Extensions_Default_Shared_DefaultExtensionHelper.htm)
[Tessa.Extensions.Default.Shared - пространство
имён](N_Tessa_Extensions_Default_Shared.htm)
