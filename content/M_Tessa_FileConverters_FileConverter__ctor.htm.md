# FileConverter - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverter(
    	IFileConverterComposer composer,
    	IDbScope dbScope
    )
VB __Копировать
     Public Sub New ( 
    	composer As IFileConverterComposer,
    	dbScope As IDbScope
    )
C++ __Копировать
     public:
    FileConverter(
    	IFileConverterComposer^ composer, 
    	IDbScope^ dbScope
    )
F# __Копировать
     new : 
            composer : IFileConverterComposer * 
            dbScope : IDbScope -> FileConverter
#### Параметры
composer
[IFileConverterComposer](T_Tessa_FileConverters_IFileConverterComposer.htm)
     Объект, выполнющий пошаговое преобразование файлов из одного формата в другой. 
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий доступ к базе данных.
##  __См. также
#### Ссылки
[FileConverter - ](T_Tessa_FileConverters_FileConverter.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
