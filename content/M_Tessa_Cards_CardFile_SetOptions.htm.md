# CardFile.SetOptions - метод
Устанавливает значение свойства [Options](P_Tessa_Cards_CardFile_Options.htm)
с выполнением сериализации указанного хранилища.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void SetOptions(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Public Sub SetOptions ( 
    	storage As Dictionary(Of String, Object)
    )
C++ __Копировать
     public:
    void SetOptions(
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     member SetOptions : 
            storage : Dictionary<string, Object> -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Хранилище, которое сериализуется в json для свойства [Options](P_Tessa_Cards_CardFile_Options.htm). Может быть равно null. 
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
