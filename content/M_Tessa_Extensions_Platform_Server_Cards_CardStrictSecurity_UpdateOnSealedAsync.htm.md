# CardStrictSecurity.UpdateOnSealedAsync - метод
Обновляет доступ к карточке при наличии ограничения
[Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task UpdateOnSealedAsync(
    	Card card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function UpdateOnSealedAsync ( 
    	card As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ UpdateOnSealedAsync(
    	Card^ card, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract UpdateOnSealedAsync : 
            card : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override UpdateOnSealedAsync : 
            card : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Обновляемая карточка.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Токен отмены асинхронной операции
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Возвращает асинхронную задачу.
#### Реализации
[ICardStrictSecurity.UpdateOnSealedAsync(Card,
CancellationToken)](M_Tessa_Extensions_Platform_Server_Cards_ICardStrictSecurity_UpdateOnSealedAsync.htm)  
##  __См. также
#### Ссылки
[CardStrictSecurity -
](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
