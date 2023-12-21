# IFileConverterRequest.FileName - свойство
Имя преобразуемого файла. При установке автоматически определяет и
устанавливает значение свойства
[Tessa.FileConverters.IFileConverterRequest.InputFormat].
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     string FileName { get; set; }
VB __Копировать
     Property FileName As String
    	Get
    	Set
C++ __Копировать
    property String^ FileName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     abstract FileName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
