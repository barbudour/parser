# IFileConverterExtension - методы
##  __Методы
[AfterRequest](M_Tessa_FileConverters_IFileConverterExtension_AfterRequest.htm)|
Метод, выполняемый после конвертирования файлов, причём как в случае успеха,
так и при возникновении ошибок. Проверить успешность операции можно по
свойству context.RequestIsSuccessful. Файл после конвертации доступен в этом
методе по заданному в контексте пути. Если метод вернёт ошибку в результате
валидации или выбросит исключение, то результаты конвертации не будут
сохранены.  
---|---  
[BeforeRequest](M_Tessa_FileConverters_IFileConverterExtension_BeforeRequest.htm)|
Метод, выполняемый перед конвертированием файлов. Файл после конвертации
недоступен в этом методе. Если метод вернёт ошибку в результате валидации или
выбросит исключение, то конвертация не будет выполнена.  
## __См. также
#### Ссылки
[IFileConverterExtension -
](T_Tessa_FileConverters_IFileConverterExtension.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
