# CardFileTypePolicy(Guid[]) - конструктор
Создаёт экземпляр класса с указанием списка допустимых идентификаторов типов
карточек для выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileTypePolicy(
    	params Guid[] cardTypeIDs
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray cardTypeIDs As Guid()
    )
C++ __Копировать
     public:
    CardFileTypePolicy(
    	... array<Guid>^ cardTypeIDs
    )
F# __Копировать
     new : 
            cardTypeIDs : Guid[] -> CardFileTypePolicy
#### Параметры
cardTypeIDs [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
     Список допустимых идентификаторов типов карточек для выполнения методов расширения. 
## __См. также
#### Ссылки
[CardFileTypePolicy - ](T_Tessa_Cards_Extensions_CardFileTypePolicy.htm)
[CardFileTypePolicy -
перегрузка](Overload_Tessa_Cards_Extensions_CardFileTypePolicy__ctor.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
