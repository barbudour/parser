# CardValidationKeys.IsCardExists - метод
Возвращает признак того, что заданный ключ относится к ошибкам вида "карточка
уже существует".
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsCardExists(
    	ValidationKey key
    )
VB __Копировать
     Public Shared Function IsCardExists ( 
    	key As ValidationKey
    ) As Boolean
C++ __Копировать
     public:
    static bool IsCardExists(
    	ValidationKey^ key
    )
F# __Копировать
     static member IsCardExists : 
            key : ValidationKey -> bool 
#### Параметры
key [ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm)
    Проверяемый ключ валидации. Может быть равен null.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданный ключ относится к ошибкам вида "карточка уже существует";
false в противном случае.
## __См. также
#### Ссылки
[CardValidationKeys - ](T_Tessa_Cards_CardValidationKeys.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
