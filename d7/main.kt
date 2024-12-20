package aoc_d7
import java.io.File
import kotlin.collections.mutableMapOf

fun main(){
    val entries = getEntries("test.txt")

    println(entries.size)

    var cnt = 0L
    for ((m,l) in entries){
        if(check(m!!, l)){
            cnt += m!!
        }
    }
    println(cnt)
}


class Node(val value: Long, val parent: Node? = null) {
    var mulNode: Node? = null
    var addNode: Node? = null

    fun getLevel(): Long {
        if(parent == null)
            return 0L
        return parent?.getLevel() + 1L
    }
}

fun check(max: Long, vals:MutableList<Long?>):Boolean{
    val root = Node(vals[0]!!)
    for(i in 0..(vals.size-2)){
        val checkList = getNodesAtLevel(root, i.toLong())
        for (n in checkList){
            addNode(n, vals[i+1]!!, max)
        }
    }
    val l = getNodesAtLevel(root, (vals.size-1).toLong())

    for (n in l){
        if (n.value == max) return true
    }
    return false
}

fun addNode(root: Node, value:Long, max:Long){
    if(root.value + value <= max ){
        root.addNode = Node(root.value + value, root)
    }
    if(root.value * value <= max){
        root.mulNode = Node(root.value * value, root)
    }
}

fun getNodesAtLevel(root: Node?, level:Long): MutableList<Node>{

    var _out = mutableListOf<Node>()

    if (root?.getLevel() == level && root != null) {
        _out.add(root)
    }

    if (root?.mulNode != null){
        _out.addAll(getNodesAtLevel(root?.mulNode, level))
    }


    if (root?.addNode != null){
        _out.addAll(getNodesAtLevel(root?.addNode, level))
    }
    return _out
}

fun getEntries(filename: String):MutableList<Pair<Long?, MutableList<Long?>>>{
    val f = File(filename).readText(Charsets.UTF_8)

    val r_d = Regex("(\\d+):(.*)")
    
    val r_d2 = Regex("\\d+") 

    val entries = r_d.findAll(f)


    var mainList = mutableListOf<Pair<Long?, MutableList<Long?>>>()
    var c = 0
    for (e in entries){
        c++
        var v = r_d2.findAll(e.groups[2]?.value ?: "")

        var k = e.groups[1]?.value

        var key = k?.trim()?.toLongOrNull()

        var vals = mutableListOf<Long?>() 
        for (m in v){
            vals.add(m.value?.toLongOrNull())
        }

        mainList.add(Pair(key, vals))
    }

    println(c)
    return mainList
}