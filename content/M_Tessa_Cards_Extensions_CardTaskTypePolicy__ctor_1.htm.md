# CardTaskTypePolicy(String[]) - конструктор
Создаёт экземпляр класса с указанием списка допустимых имён типов заданий для
выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTaskTypePolicy(
    	params string[] cardTypeNames
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray cardTypeNames As String()
    )
C++ __Копировать
     public:
    CardTaskTypePolicy(
    	... array<String^>^ cardTypeNames
    )
F# __Копировать
     new : 
            cardTypeNames : string[] -> CardTaskTypePolicy
#### Параметры
cardTypeNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список допустимых имён типов заданий для выполнения методов расширения. Значения null недопустимы. 
## __См. также
#### Ссылки
[CardTaskTypePolicy - ](T_Tessa_Cards_Extensions_CardTaskTypePolicy.htm)
[CardTaskTypePolicy -
перегрузка](Overload_Tessa_Cards_Extensions_CardTaskTypePolicy__ctor.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
