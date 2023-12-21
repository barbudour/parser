# CardHelper.DefaultDateTime - свойство
Дата и время, устанавливаемые по умолчанию в пакете карточки. Значение
представлено в формате UTC. Гарантируется, что время в UTC равно 00:00:00.
Значение отличается от [MinDateTime](P_Tessa_Cards_CardHelper_MinDateTime.htm)
для безопасного перевода между часовыми поясами, когда в структуре
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
устанавливается только время.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static DateTime DefaultDateTime { get; }
VB __Копировать
     Public Shared ReadOnly Property DefaultDateTime As DateTime
    	Get
C++ __Копировать
     public:
    static property DateTime DefaultDateTime {
    	DateTime get ();
    }
F# __Копировать
     static member DefaultDateTime : DateTime with get
#### Значение свойства
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
