# FileConverterOutputFormatPolicy - конструктор
Создаёт экземпляр класса с указанием списка допустимых выходных форматов по
конвертации файлов для выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverterOutputFormatPolicy(
    	params FileConverterFormat[] outputFormats
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray outputFormats As FileConverterFormat()
    )
C++ __Копировать
     public:
    FileConverterOutputFormatPolicy(
    	... array<FileConverterFormat>^ outputFormats
    )
F# __Копировать
     new : 
            outputFormats : FileConverterFormat[] -> FileConverterOutputFormatPolicy
#### Параметры
outputFormats
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)[]
     Список допустимых выходных форматов по конвертации файлов для выполнения методов расширения. Значения null недопустимы. 
## __См. также
#### Ссылки
[FileConverterOutputFormatPolicy -
](T_Tessa_FileConverters_FileConverterOutputFormatPolicy.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
