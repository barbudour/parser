# CardLocalizationLanguageProvider.GetAvailableUILanguagesAsync - метод
Возвращает список доступных языков интерфейса.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IReadOnlyList<LocalizationLanguage>> GetAvailableUILanguagesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAvailableUILanguagesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IReadOnlyList(Of LocalizationLanguage))
C++ __Копировать
     public:
    virtual ValueTask<IReadOnlyList<LocalizationLanguage^>^> GetAvailableUILanguagesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAvailableUILanguagesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<LocalizationLanguage>> 
    override GetAvailableUILanguagesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<LocalizationLanguage>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[LocalizationLanguage](T_Tessa_Localization_LocalizationLanguage.htm)>>  
Список доступных языков интерфейса.
#### Реализации
[ILocalizationLanguageProvider.GetAvailableUILanguagesAsync(CancellationToken)](M_Tessa_Localization_ILocalizationLanguageProvider_GetAvailableUILanguagesAsync.htm)  
##  __См. также
#### Ссылки
[CardLocalizationLanguageProvider -
](T_Tessa_Cards_CardLocalizationLanguageProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
