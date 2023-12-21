# ICardFileSourceOverrideProvider.GetOverrideSettingsAsync - метод
Возвращает объект с настройками по местоположению контента файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<ICardFileSourceOverrideSettings> GetOverrideSettingsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetOverrideSettingsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardFileSourceOverrideSettings)
C++ __Копировать
     ValueTask<ICardFileSourceOverrideSettings^> GetOverrideSettingsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetOverrideSettingsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardFileSourceOverrideSettings> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardFileSourceOverrideSettings](T_Tessa_Cards_ICardFileSourceOverrideSettings.htm)>  
Объект с настройками по местоположению контента файлов.
##  __См. также
#### Ссылки
[ICardFileSourceOverrideProvider -
](T_Tessa_Cards_ICardFileSourceOverrideProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
