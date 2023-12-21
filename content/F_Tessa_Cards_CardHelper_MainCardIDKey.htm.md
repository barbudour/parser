# CardHelper.MainCardIDKey - поле
Ключ, по которому в [!:CardNewRequest.Info] устанавливается идентификатор
основной карточки. Наличие такого идентификатора свидетельствует о том, что
создаваемую карточку следует интерпретировать как сателлит. Также используется
при сохранении карточки диалога для передачи идентификатора основной карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string MainCardIDKey = ".MainCardID"
VB __Копировать
     Public Const MainCardIDKey As String = ".MainCardID"
C++ __Копировать
     public:
    literal String^ MainCardIDKey = ".MainCardID"
F# __Копировать
     static val mutable MainCardIDKey: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
