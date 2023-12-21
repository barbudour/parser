# FileConverterRequest.OutputFormat - свойство
Выходной формат файла. Значение используется для вычисления хеша запроса.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverterFormat OutputFormat { get; set; }
VB __Копировать
     Public Property OutputFormat As FileConverterFormat
    	Get
    	Set
C++ __Копировать
     public:
    virtual property FileConverterFormat OutputFormat {
    	FileConverterFormat get () sealed;
    	void set (FileConverterFormat value) sealed;
    }
F# __Копировать
     abstract OutputFormat : FileConverterFormat with get, set
    override OutputFormat : FileConverterFormat with get, set
#### Значение свойства
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
#### Реализации
[IFileConverterRequest.OutputFormat](P_Tessa_FileConverters_IFileConverterRequest_OutputFormat.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
