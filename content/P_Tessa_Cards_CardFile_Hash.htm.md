# CardFile.Hash - свойство
Хеш контента для последней версии файла или null, если хеш не указан.
Рекомендуется указать при создании новой версии, чтобы в дальнейшем для этой
версии был доступен хеш контента. Укажите флаг
[CalculateHash](T_Tessa_Cards_CardFileFlags.htm) в свойстве
[Flags](P_Tessa_Cards_CardFile_Flags.htm) для того, чтобы при сохранении файла
хеш-сумма была вычислена на сервере, независимо от значения в свойстве Hash.
По умолчанию значение равно null, при этом для новых версий хеш считается не
заданным.
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
##  __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
