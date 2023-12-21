# CardSatelliteHelper.TryGetSatelliteCard - метод
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит не была установлена или была
установлена как отсутствующая.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetSatelliteCard(
    	Card mainCard,
    	string satelliteKey
    )
VB __Копировать
     Public Shared Function TryGetSatelliteCard ( 
    	mainCard As Card,
    	satelliteKey As String
    ) As Card
C++ __Копировать
     public:
    static Card^ TryGetSatelliteCard(
    	Card^ mainCard, 
    	String^ satelliteKey
    )
F# __Копировать
     static member TryGetSatelliteCard : 
            mainCard : Card * 
            satelliteKey : string -> Card 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлена карточка-сателлит.
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) основной карточки, который содержит хранилище карточки-сателлита, или null, если используется системный ключ по умолчанию (подходит для случаев, когда карточку сопровождает единственный сателлит). 
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточку-сателлит, которая была установлена в пакете основной карточки, или
null, если карточка-сателлит не была установлена или была установлена как
отсутствующая.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
