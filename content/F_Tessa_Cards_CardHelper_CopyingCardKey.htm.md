# CardHelper.CopyingCardKey - поле
Ключ в хеш-таблице Info в запросе на экспорт карточки
[CardGetRequest](T_Tessa_Cards_CardGetRequest.htm) или на создание по шаблону
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm). Содержит признак того, что
выполняется копирование карточки, а не обычный экспорт или создание по
шаблону. Для созданной карточки признак устанавливается в Card.Info, где его
можно увидеть в истории действий.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string CopyingCardKey = ".copyingCard"
VB __Копировать
     Public Const CopyingCardKey As String = ".copyingCard"
C++ __Копировать
     public:
    literal String^ CopyingCardKey = ".copyingCard"
F# __Копировать
     static val mutable CopyingCardKey: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
