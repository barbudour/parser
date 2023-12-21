# FmHelper.TryGetSatellite - метод
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит не была установлена или была
установлена как отсутствующая.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Forums](N_Tessa_Extensions_Default_Shared_Forums.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetSatellite(
    	Card mainCard
    )
VB __Копировать
     Public Shared Function TryGetSatellite ( 
    	mainCard As Card
    ) As Card
C++ __Копировать
     public:
    static Card^ TryGetSatellite(
    	Card^ mainCard
    )
F# __Копировать
     static member TryGetSatellite : 
            mainCard : Card -> Card 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлена карточка-сателлит.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточку-сателлит, которая была установлена в пакете основной карточки, или
null, если карточка-сателлит не была установлена или была установлена как
отсутствующая.
## __См. также
#### Ссылки
[FmHelper - ](T_Tessa_Extensions_Default_Shared_Forums_FmHelper.htm)
[Tessa.Extensions.Default.Shared.Forums - пространство
имён](N_Tessa_Extensions_Default_Shared_Forums.htm)
