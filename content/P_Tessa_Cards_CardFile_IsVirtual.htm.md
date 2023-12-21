# CardFile.IsVirtual - свойство
Признак того, что файл виртуальный, такой как "Лист согласования". Некоторые
расширения учитывают этот признак, и, например, игнорируют файл при назначении
разрешений в процессе чтения карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsVirtual { get; set; }
VB __Копировать
     Public Property IsVirtual As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool IsVirtual {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member IsVirtual : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
