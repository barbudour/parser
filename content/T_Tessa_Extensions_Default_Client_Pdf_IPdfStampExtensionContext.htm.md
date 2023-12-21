# IPdfStampExtensionContext - интерфейс
Контекст расширений
[IPdfStampExtension](T_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtension.htm),
выполняющих простановку штампов PDF для файлов карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Pdf](N_Tessa_Extensions_Default_Client_Pdf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPdfStampExtensionContext : IExtensionContext
VB __Копировать
     Public Interface IPdfStampExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IPdfStampExtensionContext : IExtensionContext
F# __Копировать
     type IPdfStampExtensionContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[Card](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Card.htm)|
Карточка, для файлов которой выполняется конвертация с простановкой штампа.  
[Context](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Context.htm)|
Внешний контекст обработки документов PDF. Обычно это объект
[IPdfGeneratorContext](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext.htm).
Может быть равен null.  
[Document](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Document.htm)|
Текущий документ PDF.  
[Editor](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Editor.htm)|
Редактируемое представление карточки
[Card](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Card.htm)
на клиенте. Позволяет выполнить сохранение или обновление карточки, или
получить информацию из контекста.  
[FileContainer](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_FileContainer.htm)|
Контейнер, управляющий файлами в карточке
[Card](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Card.htm).
Обычно средствами этого объекта могут быть добавлены или заменены файлы в
карточке.  
[FileControl](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_FileControl.htm)|
Элемент управления файлами, с которым связана текущая обработка. Обычно
средствами этого элемента управления будет добавлен или заменён файл в
карточке после генерации. Может быть равен null.  
[GeneratorContextInfo](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_GeneratorContextInfo.htm)|
Информация для расширений, существующая в рамках запроса по генерации для
объекта
[IPdfGenerator](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGenerator.htm).
Информация недоступна для изменений.  
[GeneratorInfo](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_GeneratorInfo.htm)|
Информация для расширений, заданная в генераторе, обычно это объект
[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm).
Информация недоступна для изменений.  
[Graphics](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Graphics.htm)|
Объект, предоставляющий средства рисования текста и графических примитивов
поверх страницы PDF.  
[Info](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Info.htm)|
Произвольная информация, существующая в рамках цепочки расширений.  
[Model](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Model.htm)|
Модель карточки, для файлов которой выполняется конвертация с простановкой
штампа, со средствами управления её объектами в UI.  
[Page](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_Page.htm)|
Текущая страница PDF.  
[PageNumber](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_PageNumber.htm)|
Номер текущей обрабатываемой страницы, отсчитываемый от 1 до значения
[TotalPages](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_TotalPages.htm).  
[StampWriter](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_StampWriter.htm)|
Объект, посредством которого можно настроить вывод штампа. Если штамп будет
указан непустым, то он будет выведен на текущей страницы после завершения
работы расширений.  
[TotalPages](P_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext_TotalPages.htm)|
Общее количество страниц в генерируемом документе.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Pdf - пространство
имён](N_Tessa_Extensions_Default_Client_Pdf.htm)
