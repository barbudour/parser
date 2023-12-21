# CardTypePolicy(Guid[]) - конструктор
Создаёт экземпляр класса с указанием списка допустимых идентификаторов типов
карточек для выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTypePolicy(
    	params Guid[] cardTypeIDs
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray cardTypeIDs As Guid()
    )
C++ __Копировать
     public:
    CardTypePolicy(
    	... array<Guid>^ cardTypeIDs
    )
F# __Копировать
     new : 
            cardTypeIDs : Guid[] -> CardTypePolicy
#### Параметры
cardTypeIDs [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
     Список допустимых идентификаторов типов карточек для выполнения методов расширения. 
## __См. также
#### Ссылки
[CardTypePolicy - ](T_Tessa_Cards_Extensions_CardTypePolicy.htm)
[CardTypePolicy -
перегрузка](Overload_Tessa_Cards_Extensions_CardTypePolicy__ctor.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
