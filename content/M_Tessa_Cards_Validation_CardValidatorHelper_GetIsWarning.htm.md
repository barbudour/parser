# CardValidatorHelper.GetIsWarning - метод
Возвращает признак того, что сообщение валидатора должно быть предупреждением,
а не ошибкой. Обычно сообщения-предупреждения не отображаются на клиенте,
кроме некоторых случаев работы с виртуальными секциями, которые на сервере не
могут быть проверены SQL-запросом.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool GetIsWarning(
    	CardTypeValidator validator
    )
VB __Копировать
     Public Shared Function GetIsWarning ( 
    	validator As CardTypeValidator
    ) As Boolean
C++ __Копировать
     public:
    static bool GetIsWarning(
    	CardTypeValidator^ validator
    )
F# __Копировать
     static member GetIsWarning : 
            validator : CardTypeValidator -> bool 
#### Параметры
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Объект, содержащий настройки валидатора.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что сообщение валидатора должно быть предупреждением, а не
ошибкой.
##  __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
