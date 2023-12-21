# KrPermissionsHelper.GetUnavailableTypesAsync - метод
Возвращает список недоступных имен для создания эффективных (типы карточек, не
использующие типы документов и типы документов) типов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<(ReadOnlyCollection<Guid> , ValidationResult )> GetUnavailableTypesAsync(
    	ICardRepository cardRepository,
    	IKrTypesCache krTypesCache,
    	bool includeHiddenTypes = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetUnavailableTypesAsync ( 
    	cardRepository As ICardRepository,
    	krTypesCache As IKrTypesCache,
    	Optional includeHiddenTypes As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ( As ReadOnlyCollection(Of Guid),  As ValidationResult))
C++ __Копировать
     public:
    static Task<ValueTuple<ReadOnlyCollection<Guid>^, ValidationResult^>>^ GetUnavailableTypesAsync(
    	ICardRepository^ cardRepository, 
    	IKrTypesCache^ krTypesCache, 
    	bool includeHiddenTypes = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetUnavailableTypesAsync : 
            cardRepository : ICardRepository * 
            krTypesCache : IKrTypesCache * 
            ?includeHiddenTypes : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _includeHiddenTypes = defaultArg includeHiddenTypes false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<ReadOnlyCollection<Guid>, ValidationResult>> 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий карточек
krTypesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
    Кеш типов
includeHiddenTypes
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    Включать ли скрытые типы
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>,
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>>  
Возвращает список недоступных имен для создания эффективных типов.
##  __См. также
#### Ссылки
[KrPermissionsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
