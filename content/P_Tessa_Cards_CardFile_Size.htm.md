# CardFile.Size - свойство
Размер контента последней версии файла в байтах или -1, если размер неизвестен
или не был задан. В серверных расширениях на сохранение это свойство можно
использовать для определения размера контента сохраняемых файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public long Size { get; set; }
VB __Копировать
     Public Property Size As Long
    	Get
    	Set
C++ __Копировать
     public:
    property long long Size {
    	long long get ();
    	void set (long long value);
    }
F# __Копировать
     member Size : int64 with get, set
#### Значение свойства
[Int64](https://learn.microsoft.com/dotnet/api/system.int64)
##  __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
