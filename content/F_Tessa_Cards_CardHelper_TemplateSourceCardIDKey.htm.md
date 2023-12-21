# CardHelper.TemplateSourceCardIDKey - поле
Ключ в хеш-таблице Info в запросе на создание карточки по шаблону
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm), который содержит
идентификатор карточки, по которой создаётся новая карточка. Это может быть
как идентификатор карточки шаблона, если карточка создаётся по шаблону, так и
идентификатор копируемой карточки, если выполняется копирование карточки
(через плитку "Копировать"). Если карточка копируется, то в Info будет признак
[CopyingCardKey](F_Tessa_Cards_CardHelper_CopyingCardKey.htm). Также ключ
может отсутствовать в Info, например, если карточка создаётся по шаблону из
экспортированной в файл карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string TemplateSourceCardIDKey = ".templateSourceCardID"
VB __Копировать
     Public Const TemplateSourceCardIDKey As String = ".templateSourceCardID"
C++ __Копировать
     public:
    literal String^ TemplateSourceCardIDKey = ".templateSourceCardID"
F# __Копировать
     static val mutable TemplateSourceCardIDKey: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
