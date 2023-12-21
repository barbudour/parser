# MultitypeSatelliteDeleteExtension.CreateSatelliteInfoAsync - метод
Создаёт информацию по карточке-сателлиту, которая относится к текущему
расширению.
##  __Definition
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
    Карточка-сателлит.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm)>  
Информация по карточке-сателлиту, которая относится к текущему расширению.
##  __См. также
#### Ссылки
[MultitypeSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
