# CardValidatorHelper.TryGetErrorMessage - метод
Возвращает сообщение об ошибке, которое следует выводить вместо стандартного
сообщения, или null или пустая строка, если сообщение не задано.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string TryGetErrorMessage(
    	CardTypeValidator validator
    )
VB __Копировать
     Public Shared Function TryGetErrorMessage ( 
    	validator As CardTypeValidator
    ) As String
C++ __Копировать
     public:
    static String^ TryGetErrorMessage(
    	CardTypeValidator^ validator
    )
F# __Копировать
     static member TryGetErrorMessage : 
            validator : CardTypeValidator -> string 
#### Параметры
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Объект, содержащий настройки валидатора.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Сообщение об ошибке, которое следует выводить вместо стандартного сообщения,
или null или пустая строка, если сообщение не задано.
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
