# IFileConverterRequest.OutputFormat - свойство
Выходной формат файла. Значение используется для вычисления хеша запроса.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    FileConverterFormat OutputFormat { get; set; }
VB __Копировать
     Property OutputFormat As FileConverterFormat
    	Get
    	Set
C++ __Копировать
    property FileConverterFormat OutputFormat {
    	FileConverterFormat get ();
    	void set (FileConverterFormat value);
    }
F# __Копировать
     abstract OutputFormat : FileConverterFormat with get, set
#### Значение свойства
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
