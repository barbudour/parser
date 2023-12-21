# CardHelper.CopyFilesAsync - метод
Создаёт копии файлов карточки sourceCard в карточке targetCard. При этом не
выполняется расширений, но учитываются все те же особенности, что и при
создании карточек по шаблону. Подписи файла по умолчанию не переносятся, если
не указан параметр copySignatures.
Фактическая копия файла с контентом будет создана после сохранения карточки
targetCard. Метод может вызываться как на сервере, так и на клиенте (причём
сервер не будет вызван).
Метод возвращает результат копирования, который не равен null и содержит
ошибки, если копирование не было выполнено.
Т.к. в карточке targetCard могут быть добавлены файлы, то карточку
рекомендуется сохранять посредством
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm), чтобы содержимое
файлов было корректно скопировано.
При сохранении посредством
[ICardRepository](T_Tessa_Cards_ICardRepository.htm) файлы будут добавлены без
содержимого.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<ValidationResult> CopyFilesAsync(
    	Card sourceCard,
    	Card targetCard,
    	IUnityContainer unityContainer,
    	bool copyVirtual = false,
    	bool copySignatures = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CopyFilesAsync ( 
    	sourceCard As Card,
    	targetCard As Card,
    	unityContainer As IUnityContainer,
    	Optional copyVirtual As Boolean = false,
    	Optional copySignatures As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ValidationResult)
C++ __Копировать
     public:
    static ValueTask<ValidationResult^> CopyFilesAsync(
    	Card^ sourceCard, 
    	Card^ targetCard, 
    	IUnityContainer^ unityContainer, 
    	bool copyVirtual = false, 
    	bool copySignatures = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CopyFilesAsync : 
            sourceCard : Card * 
            targetCard : Card * 
            unityContainer : IUnityContainer * 
            ?copyVirtual : bool * 
            ?copySignatures : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _copyVirtual = defaultArg copyVirtual false
            let _copySignatures = defaultArg copySignatures false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
#### Параметры
sourceCard [Card](T_Tessa_Cards_Card.htm)
    Карточка, файлы которой требуется скопировать.
targetCard [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которую должны быть добавлены файлы-копии.
unityContainer IUnityContainer
    Контейнер Unity со всеми зависимостями, связанными с карточками.
copyVirtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что виртуальные файлы также копируются вместе со всеми остальными файлами.
copySignatures
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что вместе с файлом копируются подписи для последних версий файла из данных карточки sourceCard. Подписи должны быть обязательно загружены в файлах карточки sourceCard вместе с массивом байт самой подписи Data. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат копирования, который не равен null. Содержит ошибки, если
копирование не было выполнено.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
