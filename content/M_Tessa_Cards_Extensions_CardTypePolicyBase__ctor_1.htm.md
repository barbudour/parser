# CardTypePolicyBase(String[]) - конструктор
Создаёт экземпляр класса с указанием списка допустимых имён типов карточек для
выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected CardTypePolicyBase(
    	params string[] cardTypeNames
    )
VB __Копировать
     Protected Sub New ( 
    	ParamArray cardTypeNames As String()
    )
C++ __Копировать
     protected:
    CardTypePolicyBase(
    	... array<String^>^ cardTypeNames
    )
F# __Копировать
     new : 
            cardTypeNames : string[] -> CardTypePolicyBase
#### Параметры
cardTypeNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список допустимых имён типов карточек для выполнения методов расширения. Значения null недопустимы. 
## __См. также
#### Ссылки
[CardTypePolicyBase - ](T_Tessa_Cards_Extensions_CardTypePolicyBase.htm)
[CardTypePolicyBase -
перегрузка](Overload_Tessa_Cards_Extensions_CardTypePolicyBase__ctor.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
