# CardTask.IsHidden - свойство
Признак того, что задание не следует показывать в UI несмотря на то, что оно
присутствует в карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsHidden { get; set; }
VB __Копировать
     Public Property IsHidden As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool IsHidden {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member IsHidden : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Это свойство не записывается в хранилище, поэтому оно эффективно только для
текущего декоратора.
## __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
