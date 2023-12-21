# CardFileVersion.Hash - свойство
Хеш контента для сохранённой версии файла или null, если версия файла новая
или хеш не указан. По умолчанию значение равно null, при этом для новых версий
хеш считается не заданным. Изменение этого значения позволяет установить
другой хеш для использования в расширениях, но не позволяет изменить хеш у
версии. Для установки хеша создаваемой версии укажите свойство
[Hash](P_Tessa_Cards_CardFile_Hash.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public byte[] Hash { get; set; }
VB __Копировать
     Public Property Hash As Byte()
    	Get
    	Set
C++ __Копировать
     public:
    property array<unsigned char>^ Hash {
    	array<unsigned char>^ get ();
    	void set (array<unsigned char>^ value);
    }
F# __Копировать
     member Hash : byte[] with get, set
#### Значение свойства
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
##  __Заметки
Свойство заполняется платформой. Если оно не заполнено, то принимается равным
null.
## __См. также
#### Ссылки
[CardFileVersion - ](T_Tessa_Cards_CardFileVersion.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
