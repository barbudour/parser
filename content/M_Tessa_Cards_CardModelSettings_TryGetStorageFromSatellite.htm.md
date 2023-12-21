# CardModelSettings.TryGetStorageFromSatellite - метод
Возвращает хранилище с сериализованным объектом, который можно использовать в
методе [SetupFromAsync(Dictionary<String, Object>, Func<Action,
CancellationToken, Task>,
CancellationToken)](M_Tessa_Cards_CardModelSettings_SetupFromAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Dictionary<string, Object> TryGetStorageFromSatellite(
    	Card personalRoleSattelite
    )
VB __Копировать
     Public Shared Function TryGetStorageFromSatellite ( 
    	personalRoleSattelite As Card
    ) As Dictionary(Of String, Object)
C++ __Копировать
     public:
    static Dictionary<String^, Object^>^ TryGetStorageFromSatellite(
    	Card^ personalRoleSattelite
    )
F# __Копировать
     static member TryGetStorageFromSatellite : 
            personalRoleSattelite : Card -> Dictionary<string, Object> 
#### Параметры
personalRoleSattelite [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит с настройками сотрудника.
#### Возвращаемое значение
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Хранилище с сериализованным объектом.
##  __См. также
#### Ссылки
[CardModelSettings - ](T_Tessa_Cards_CardModelSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
