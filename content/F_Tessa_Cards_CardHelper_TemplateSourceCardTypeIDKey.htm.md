# CardHelper.TemplateSourceCardTypeIDKey - поле
Ключ в хеш-таблице Info в запросе на создание карточки по шаблону
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm), который содержит
идентификатор типа карточки, по которой создаётся новая карточка. Это может
быть как идентификатор типа шаблона
[TemplateTypeID](F_Tessa_Cards_CardHelper_TemplateTypeID.htm), если карточка
создаётся по шаблону, так и идентификатор типа копируемой карточки, если
выполняется копирование карточки (через плитку "Копировать"). Если карточка
копируется, то в Info будет признак
[CopyingCardKey](F_Tessa_Cards_CardHelper_CopyingCardKey.htm). Также ключ
может отсутствовать в Info, например, если карточка создаётся по шаблону из
экспортированной в файл карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string TemplateSourceCardTypeIDKey = ".templateSourceCardTypeID"
VB __Копировать
     Public Const TemplateSourceCardTypeIDKey As String = ".templateSourceCardTypeID"
C++ __Копировать
     public:
    literal String^ TemplateSourceCardTypeIDKey = ".templateSourceCardTypeID"
F# __Копировать
     static val mutable TemplateSourceCardTypeIDKey: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
