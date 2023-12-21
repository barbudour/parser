# FileConverterHelper.OldestPreviewRequestTimeKey - поле
Самая поздняя разрешённая дата, когда выполнялось обращение к файлу в кэше.
Все файлы, к которым обращались раньше это даты, будут удалены из кэша.
Укажите такую дату по этому ключу в запросе на сохранение карточки файловых
конвертеров. Значение null указывает, что из кэша будут удалены все файлы.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string OldestPreviewRequestTimeKey = ".oldestPreviewRequestTime"
VB __Копировать
     Public Const OldestPreviewRequestTimeKey As String = ".oldestPreviewRequestTime"
C++ __Копировать
     public:
    literal String^ OldestPreviewRequestTimeKey = ".oldestPreviewRequestTime"
F# __Копировать
     static val mutable OldestPreviewRequestTimeKey: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[FileConverterHelper - ](T_Tessa_FileConverters_FileConverterHelper.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
