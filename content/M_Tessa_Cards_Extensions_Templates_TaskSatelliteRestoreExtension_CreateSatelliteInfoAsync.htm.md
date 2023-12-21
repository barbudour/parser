# TaskSatelliteRestoreExtension.CreateSatelliteInfoAsync - метод
Создаёт объект с информацией по файлам карточки-сателлита на основании данных
указанной карточки-сателлита.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<SatelliteInfo> CreateSatelliteInfoAsync(
    	Card satelliteCard,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function CreateSatelliteInfoAsync ( 
    	satelliteCard As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SatelliteInfo)
C++ __Копировать
     protected:
    virtual ValueTask<SatelliteInfo^> CreateSatelliteInfoAsync(
    	Card^ satelliteCard, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract CreateSatelliteInfoAsync : 
            satelliteCard : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SatelliteInfo> 
#### Параметры
satelliteCard [Card](T_Tessa_Cards_Card.htm)
     Карточка-сателлит, по данным которой требуется получить объект с информацией по файлам. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm)>  
Объект с информацией по файлам карточки-сателлита на основании данных
указанной карточки-сателлита.
## __См. также
#### Ссылки
[TaskSatelliteRestoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteRestoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
