# CardHeaderFile.Order - свойство
Порядковый номер следования файла в потоке. Чем меньше номер, тем раньше файл
должен располагаться в потоке.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int Order { get; set; }
VB __Копировать
     Public Property Order As Integer
    	Get
    	Set
C++ __Копировать
     public:
    property int Order {
    	int get ();
    	void set (int value);
    }
F# __Копировать
     member Order : int with get, set
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
Допустимы любые значения, в том числе и отрицательные.
## __Заметки
Если у всех файлов задан порядок следования Order равный 0 (по умолчанию), то
файлы будут отсортированы по идентификаторам
[ID](P_Tessa_Cards_ComponentModel_CardHeaderFile_ID.htm).
## __См. также
#### Ссылки
[CardHeaderFile - ](T_Tessa_Cards_ComponentModel_CardHeaderFile.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
