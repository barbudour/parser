# PdfStampExtensionContext - класс
Контекст расширений
[IPdfStampExtension](T_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtension.htm),
выполняющих простановку штампов PDF для файлов карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Pdf](N_Tessa_Extensions_Default_Client_Pdf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PdfStampExtensionContext : IPdfStampExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class PdfStampExtensionContext
    	Implements IPdfStampExtensionContext, IExtensionContext
C++ __Копировать
     public ref class PdfStampExtensionContext sealed : IPdfStampExtensionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type PdfStampExtensionContext = 
        class
            interface IPdfStampExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PdfStampExtensionContext
Implements
    [IPdfStampExtensionContext](T_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[PdfStampExtensionContext](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_CancellationToken.htm)|  
---|---  
[Card](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Card.htm)|
Карточка, для файлов которой выполняется конвертация с простановкой штампа.  
[Context](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Context.htm)|
Внешний контекст обработки документов PDF. Обычно это объект
[IPdfGeneratorContext](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext.htm).
Может быть равен null.  
[Document](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Document.htm)|
Текущий документ PDF.  
[Editor](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Editor.htm)|
Редактируемое представление карточки
[Card](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Card.htm)
на клиенте. Позволяет выполнить сохранение или обновление карточки, или
получить информацию из контекста.  
[FileContainer](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_FileContainer.htm)|
Контейнер, управляющий файлами в карточке
[Card](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Card.htm).
Обычно средствами этого объекта могут быть добавлены или заменены файлы в
карточке.  
[FileControl](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_FileControl.htm)|
Элемент управления файлами, с которым связана текущая обработка. Обычно
средствами этого элемента управления будет добавлен или заменён файл в
карточке после генерации. Может быть равен null.  
[GeneratorContextInfo](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_GeneratorContextInfo.htm)|
Информация для расширений, существующая в рамках запроса по генерации для
объекта
[IPdfGenerator](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGenerator.htm).
Информация недоступна для изменений.  
[GeneratorInfo](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_GeneratorInfo.htm)|
Информация для расширений, заданная в генераторе, обычно это объект
[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm).
Информация недоступна для изменений.  
[Graphics](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Graphics.htm)|
Объект, предоставляющий средства рисования текста и графических примитивов
поверх страницы PDF.  
[Info](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Info.htm)|
Произвольная информация, существующая в рамках цепочки расширений.  
[Model](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Model.htm)|
Модель карточки, для файлов которой выполняется конвертация с простановкой
штампа, со средствами управления её объектами в UI.  
[Page](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Page.htm)|
Текущая страница PDF.  
[PageNumber](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_PageNumber.htm)|
Номер текущей обрабатываемой страницы, отсчитываемый от 1 до значения
[TotalPages](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_TotalPages.htm).  
[StampWriter](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_StampWriter.htm)|
Объект, посредством которого можно настроить вывод штампа. Если штамп будет
указан непустым, то он будет выведен на текущей страницы после завершения
работы расширений.  
[TotalPages](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_TotalPages.htm)|
Общее количество страниц в генерируемом документе.  
## __Методы
[ClearPage](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_ClearPage.htm)|
Очищает информацию по странице PDF в свойствах
[Page](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Page.htm),
[Graphics](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_Graphics.htm)
и
[PageNumber](P_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_PageNumber.htm).
Вызовите метод, чтобы предотвратить утечки памяти после того, как объект уже
не требуется использовать. Не используйте объект после вызова этого метода,
кроме случаев, когда позже вызывается метод [SetPage(PdfPage, XGraphics,
Int32)](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_SetPage.htm).  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetPage](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensionContext_SetPage.htm)|
Изменяет текущую страницу PDF в контексте расширения.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Pdf - пространство
имён](N_Tessa_Extensions_Default_Client_Pdf.htm)
